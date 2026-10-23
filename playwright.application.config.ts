import { defineConfig } from '@playwright/test';
if(!process.env.QA_APP_URL)throw new Error('Set QA_APP_URL to the actual approved application target.');
if(process.env.QA_APPLICATION_SCOPE_CONFIRMED!=='true')throw new Error('Confirm the actual target/data scope using QA_APPLICATION_SCOPE_CONFIRMED=true.');
export default defineConfig({testDir:'./automation/application',testMatch:'**/*.spec.ts',forbidOnly:true,retries:0,
  reporter:[['list'],['html',{outputFolder:'reports/application/html',open:'never'}]],
  use:{baseURL:process.env.QA_APP_URL,trace:'retain-on-failure',screenshot:'only-on-failure'}});
