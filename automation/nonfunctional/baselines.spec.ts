import AxeBuilder from '@axe-core/playwright';
import { test, expect } from '../fixtures/test';
test('NFR-01 accessibility checks agreed automated WCAG A/AA rules on the local page',async({page,workspace})=>{
  await page.goto('/?workspace='+workspace);await expect(page.getByRole('heading',{level:1})).toBeVisible();
  const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
  expect(result.violations).toEqual([]);
});
test('NFR-02 keyboard interaction can create a record',async({page,api,workspace})=>{
  await page.goto('/?workspace='+workspace);await page.getByLabel('Record name').focus();await page.keyboard.type('Keyboard record');
  await page.keyboard.press('Tab');await expect(page.getByRole('button',{name:'Create record',exact:true})).toBeFocused();
  await page.keyboard.press('Enter');await expect(page.getByRole('status')).toHaveText('Record created.');expect(await (await api.list()).json()).toHaveLength(1);
});
test('NFR-03 response configuration prevents caching and MIME sniffing',async({request})=>{
  const response=await request.get('/');expect(response.headers()['cache-control']).toBe('no-store');expect(response.headers()['x-content-type-options']).toBe('nosniff');
});
