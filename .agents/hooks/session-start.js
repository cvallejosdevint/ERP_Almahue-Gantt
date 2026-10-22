#!/usr/bin/env node
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const script = path.join(__dirname, '..', 'scripts', 'start-local-stack.ps1');

function kickLocalStack() {
  if (!fs.existsSync(script)) return;
  const child = spawn(
    'powershell.exe',
    ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', script],
    { detached: true, stdio: 'ignore', windowsHide: true },
  );
  child.unref();
}

try {
  kickLocalStack();
} catch {
  /* fail open: no bloquear la sesión si el arranque local falla */
}

let buf = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (c) => {
  buf += c;
});
process.stdin.on('end', () => {
  process.stdout.write(
    JSON.stringify({
      additional_context:
        'ERP Almahue: lee AGENTS.md. Skills: almahue-erp-contexto, almahue-aprobaciones, almahue-deploy, almahue-modulo, almahue-qa-local. No leas transcripciones salvo pedido explícito. Stack local (si el puerto está libre): ERP API :3001, front :5174, billing-gateway :3040 vía .cursor/scripts/start-local-stack.ps1.',
    }),
  );
});
