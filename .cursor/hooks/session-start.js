#!/usr/bin/env node
let buf = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (c) => {
  buf += c;
});
process.stdin.on('end', () => {
  process.stdout.write(
    JSON.stringify({
      additional_context:
        'ERP Almahue: lee AGENTS.md. Skills: almahue-erp-contexto, almahue-aprobaciones, almahue-deploy, almahue-modulo, almahue-qa-local. No leas transcripciones salvo pedido explícito.',
    }),
  );
});
