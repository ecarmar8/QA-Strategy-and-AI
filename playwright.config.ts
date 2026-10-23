import { defineConfig, devices } from '@playwright/test';
const port = Number(process.env.QA_CONTRACT_PORT || 4317);
const baseURL = `http://127.0.0.1:${port}`;
export default defineConfig({
  testDir: './automation',
  timeout: 30_000,
  expect: { timeout: 5_000 },
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  reporter: [['list'], ['html', { outputFolder: 'reports/automation/html', open: 'never' }],
    ['junit', { outputFile: 'reports/automation/junit.xml' }],
    ['json', { outputFile: 'reports/automation/results.json' }]],
  outputDir: 'reports/automation/artifacts',
  use: {
    baseURL,
    trace: 'retain-on-failure', screenshot: 'only-on-failure',
    headless: process.env.QA_HEADED !== 'true',
    launchOptions: {
      ...(process.env.QA_BROWSER_EXECUTABLE ? { executablePath: process.env.QA_BROWSER_EXECUTABLE } : {}),
      ...(process.env.QA_BROWSER_ARGS ? { args: JSON.parse(process.env.QA_BROWSER_ARGS) } : {}),
    },
  },
  webServer: { command: 'node automation/support/contract-server.mjs', url: `${baseURL}/health`,
    reuseExistingServer: false, timeout: 20_000, env: { QA_CONTRACT_PORT: String(port) } },
  projects: [
    { name: 'chromium-ui', testMatch: /ui\/.*\.spec\.ts/, use: { ...devices['Desktop Chrome'] } },
    { name: 'quality-attributes', testMatch: /nonfunctional\/.*\.spec\.ts/, use: { ...devices['Desktop Chrome'] } },
  ],
});
