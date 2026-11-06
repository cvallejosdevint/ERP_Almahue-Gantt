const fs = require('fs');

// 1. Patch domain.ts
let domain = fs.readFileSync('ERP/erp_front/src/types/domain.ts', 'utf8');
const domainTarget = '  requiereVariedad?: boolean;\r\n  requiereVencimiento?: boolean;';
const domainRepl = '  requiereVariedad?: boolean;\r\n  requiereAux?: boolean;\r\n  requiereRef?: boolean;\r\n  requiereVencimiento?: boolean;';
if (!domain.includes(domainTarget)) {
  if (domain.includes('requiereAux?: boolean;')) {
    console.log('domain.ts already contains requiereAux');
  } else {
    console.error('domainTarget not found');
  }
} else {
  domain = domain.replace(domainTarget, domainRepl);
  fs.writeFileSync('ERP/erp_front/src/types/domain.ts', domain, 'utf8');
  console.log('domain.ts patched successfully');
}

// 2. Patch PlanCuentasPage.tsx
let page = fs.readFileSync('ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx', 'utf8');

// 2.1 CuentaFlagPatch
const p1Target = "| 'requiereVariedad'\r\n    | 'requiereVencimiento'";
const p1Repl = "| 'requiereVariedad'\r\n    | 'requiereAux'\r\n    | 'requiereRef'\r\n    | 'requiereVencimiento'";
if (!page.includes(p1Target)) console.error('p1Target not found');
else page = page.replace(p1Target, p1Repl);

// 2.2 Table rows AUX & REF
const p2Target = '<td className="w-9 py-1 text-center"><PlanFlagCheckbox checked={false} disabled ariaLabel={`AUX ${node.codigo}`} /></td>\r\n        <td className="w-9 py-1 text-center"><PlanFlagCheckbox checked={false} disabled ariaLabel={`REF ${node.codigo}`} /></td>';
const p2Repl = `<td className="w-9 py-1 text-center">
          <PlanFlagCheckbox
            checked={Boolean(node.requiereAux)}
            disabled={busy}
            ariaLabel={\`AUX \${node.codigo}\`}
            onChange={(v) => patch('requiereAux', v)}
          />
        </td>
        <td className="w-9 py-1 text-center">
          <PlanFlagCheckbox
            checked={Boolean(node.requiereRef)}
            disabled={busy}
            ariaLabel={\`REF \${node.codigo}\`}
            onChange={(v) => patch('requiereRef', v)}
          />
        </td>`;
if (!page.includes(p2Target)) console.error('p2Target not found');
else page = page.replace(p2Target, p2Repl);

// 2.3 Form state hooks
const p3Target = '  const [formReqVariedad, setFormReqVariedad] = useState(false);\r\n  const [formReqVcto, setFormReqVcto] = useState(false);';
const p3Repl = '  const [formReqVariedad, setFormReqVariedad] = useState(false);\r\n  const [formReqAux, setFormReqAux] = useState(false);\r\n  const [formReqRef, setFormReqRef] = useState(false);\r\n  const [formReqVcto, setFormReqVcto] = useState(false);';
if (!page.includes(p3Target)) console.error('p3Target not found');
else page = page.replace(p3Target, p3Repl);

// 2.4 openCreateChild resets
const p4Target = '    setFormReqVariedad(false);\r\n    setFormReqVcto(false);';
const p4Repl = '    setFormReqVariedad(false);\r\n    setFormReqAux(false);\r\n    setFormReqRef(false);\r\n    setFormReqVcto(false);';
if (!page.includes(p4Target)) console.error('p4Target not found');
else page = page.replace(p4Target, p4Repl);

// 2.5 loadFormFromRow
const p5Target = '    setFormReqVariedad(Boolean(row.requiereVariedad));\r\n    setFormReqVcto(Boolean(row.requiereVencimiento));';
const p5Repl = '    setFormReqVariedad(Boolean(row.requiereVariedad));\r\n    setFormReqAux(Boolean(row.requiereAux));\r\n    setFormReqRef(Boolean(row.requiereRef));\r\n    setFormReqVcto(Boolean(row.requiereVencimiento));';
if (!page.includes(p5Target)) console.error('p5Target not found');
else page = page.replace(p5Target, p5Repl);

// 2.6 cuentaPayloadFromRow
const p6Target = '    requiereVariedad: patch.requiereVariedad ?? Boolean(row.requiereVariedad),\r\n    requiereVencimiento: patch.requiereVencimiento ?? Boolean(row.requiereVencimiento),';
const p6Repl = '    requiereVariedad: patch.requiereVariedad ?? Boolean(row.requiereVariedad),\r\n    requiereAux: patch.requiereAux ?? Boolean(row.requiereAux),\r\n    requiereRef: patch.requiereRef ?? Boolean(row.requiereRef),\r\n    requiereVencimiento: patch.requiereVencimiento ?? Boolean(row.requiereVencimiento),';
if (!page.includes(p6Target)) console.error('p6Target not found');
else page = page.replace(p6Target, p6Repl);

// 2.7 saveCuenta payload
const p7Target = '        requiereVariedad: formReqVariedad,\r\n        requiereVencimiento: formReqVcto,';
const p7Repl = '        requiereVariedad: formReqVariedad,\r\n        requiereAux: formReqAux,\r\n        requiereRef: formReqRef,\r\n        requiereVencimiento: formReqVcto,';
if (!page.includes(p7Target)) console.error('p7Target not found');
else page = page.replace(p7Target, p7Repl);

// 2.8 Edit modal checkboxes
const p8Target = '            <Checkbox label="VAR (variedad)" checked={formReqVariedad} onChange={(e) => setFormReqVariedad(e.target.checked)} />\r\n            <Checkbox label="VCTO (vencimiento)" checked={formReqVcto} onChange={(e) => setFormReqVcto(e.target.checked)} />';
const p8Repl = '            <Checkbox label="VAR (variedad)" checked={formReqVariedad} onChange={(e) => setFormReqVariedad(e.target.checked)} />\r\n            <Checkbox label="AUX (auxiliar / RUT)" checked={formReqAux} onChange={(e) => setFormReqAux(e.target.checked)} />\r\n            <Checkbox label="REF (referencia DTE)" checked={formReqRef} onChange={(e) => setFormReqRef(e.target.checked)} />\r\n            <Checkbox label="VCTO (vencimiento)" checked={formReqVcto} onChange={(e) => setFormReqVcto(e.target.checked)} />';
if (!page.includes(p8Target)) console.error('p8Target not found');
else page = page.replace(p8Target, p8Repl);

fs.writeFileSync('ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx', page, 'utf8');
console.log('PlanCuentasPage.tsx patched successfully');

