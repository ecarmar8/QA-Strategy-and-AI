import { test, expect } from '../fixtures/test';
test.beforeEach(async({page,workspace})=>{await page.goto('/?workspace='+workspace)});
test('UI-01 @critical creates through UI and verifies the persisted API effect',async({page,api})=>{
  await page.getByLabel('Record name').fill('Cross-layer record');await page.getByRole('button',{name:'Create record',exact:true}).click();
  await expect(page.getByRole('status')).toHaveText('Record created.');
  await expect(page.getByRole('listitem')).toContainText('Cross-layer record — open');
  const rows=await (await api.list()).json();expect(rows).toHaveLength(1);expect(rows[0].name).toBe('Cross-layer record');
  await page.reload();await expect(page.getByRole('listitem')).toContainText('Cross-layer record — open');
});
test('UI-02 invalid input exposes a useful error without creating data',async({page,api})=>{
  await page.getByRole('button',{name:'Create record',exact:true}).click();await expect(page.getByRole('alert')).toContainText('Enter a name');
  expect(await (await api.list()).json()).toEqual([]);
});
test('UI-03 completes a record and verifies the underlying state',async({page,api})=>{
  const item=await (await api.create('Complete this record')).json();await page.reload();
  await page.getByRole('button',{name:'Complete Complete this record',exact:true}).click();
  await expect(page.getByRole('listitem')).toContainText('Complete this record — completed');
  expect((await (await api.get(item.id)).json()).status).toBe('completed');
});
