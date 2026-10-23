import { test as base, expect, APIRequestContext } from '@playwright/test';
import { randomUUID } from 'node:crypto';
export class RecordsApi {
  constructor(readonly request: APIRequestContext, readonly workspace: string) {}
  headers(extra: Record<string,string> = {}) { return { Authorization: 'Bearer qa-local-contract', 'x-workspace-id': this.workspace, ...extra }; }
  create(name: string, extra: Record<string,string> = {}) { return this.request.post('/api/records', { headers: this.headers(extra), data: { name } }); }
  list() { return this.request.get('/api/records', { headers: this.headers() }); }
  get(id: string) { return this.request.get(`/api/records/${id}`, { headers: this.headers() }); }
  update(id: string, status: string) { return this.request.patch(`/api/records/${id}`, { headers: this.headers(), data: { status } }); }
  remove(id: string) { return this.request.delete(`/api/records/${id}`, { headers: this.headers() }); }
  async createWithRetry(name: string, maxRetries: number, extra: Record<string,string>) {
    let response = await this.create(name, extra);
    for(let attempt=0;attempt<maxRetries&&response.status()===429;attempt++) {
      const delay = Number(response.headers()['retry-after']);
      if(!Number.isFinite(delay)||delay<0||delay>2) throw new Error('Retry delay outside the approved local contract');
      await new Promise(resolve=>setTimeout(resolve,delay*1000));
      response=await this.create(name,extra);
    }
    return response;
  }
}
export const test=base.extend<{ api: RecordsApi; workspace: string }>({
  workspace: async ({},use)=>use('qa-'+randomUUID()),
  api: async ({request,workspace},use)=>{
    const api=new RecordsApi(request,workspace);
    try { await use(api); } finally {
      const response=await api.list();
      if(!response.ok())throw new Error('Fixture cleanup cannot list created data');
      for(const item of await response.json())expect((await api.remove(item.id)).status()).toBe(204);
    }
  },
});
export { expect };
