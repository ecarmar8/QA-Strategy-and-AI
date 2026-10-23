# Export cases to Azure Test Plans

Open [test-case-export.html](../test-case-export.html) locally. It works without a server, account or API token. Select cases, supply your actual **Area Path**, **Assigned To** and permitted **State**, then download the CSV. Load another reviewed JSON catalog to export product cases using the same schema as [data/test-cases.json](../data/test-cases.json).

Alternatively:

```bash
npm run export:azure -- --area "YourProject\YourArea" --assigned "your-user@example.com" --state Design
```

Use `--input` and `--output` to change source/destination. The CLI refuses to invent missing project fields. Example values in instructions are not verified organization paths or identities.

## Format and import

The export uses UTF-8 with BOM, CRLF, quoted/escaped cells and these exact headers:

`ID,Work Item Type,Title,Test Step,Step Action,Step Expected,Area Path,Assigned To,State`

Each step is a separate row. Case reference and title repeat for all its steps; numbering restarts at 1. IDs remain blank to create new cases. A local reference such as UI-01 is part of the title, not an Azure work item ID. Source catalog and case definitions remain separate from execution results.

In Azure: **Test Plans → plan → suite → Import test cases from CSV/XLSX**. Select the CSV, review field mappings and import. Confirm that your account has the relevant Test Plans permissions and that your process accepts your field values. No tenant import has been performed by this repository.

A second import with blank IDs creates additional cases. To update, first export the existing cases from Azure and retain their real IDs. Reimporting an existing ID replaces its steps, so preserve the complete intended step list. This exporter deliberately creates new cases only.

## Source catalog

```json
{
  "schemaVersion": 1,
  "scope": "Confirmed product workflow and version",
  "cases": [{
    "id": "CASE-001",
    "title": "Reviewed business behavior",
    "layer": "UI",
    "source": "Approved requirement reference",
    "steps": [{"action": "Perform the documented action", "expected": "Observe the confirmed outcome"}]
  }]
}
```

Review AI-generated cases before import. The included API cases refer to ordered Postman requests; their setup requires running the specified predecessor requests to create their variables and records. Executing a downstream request alone is not an independent API test.

Export validation checks case identity, required action/oracle pairs, selection, spreadsheet formula prefixes and correct CSV escaping. It does not validate your Azure organization's paths, users, custom fields or policies. Importing manual cases does not automatically associate automated tests or publish run results; use the pipeline separately.

[Microsoft format and import specification](https://learn.microsoft.com/en-us/azure/devops/test/bulk-import-export-test-cases?view=azure-devops).
