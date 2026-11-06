const fs = require('fs');
let file = fs.readFileSync('docs/sesiones/compras-mejoras-modulo2-2026-10-30/recorrido.html', 'utf8');

const t1 = `        pins: [
          { x: 30, y: 35, label: "Bloque Verde: Proformas centralizadas del periodo" },
          { x: 70, y: 35, label: "Bloque Gris: Proformas pendientes o fuera de periodo" }
        ],`;
const r1 = `        pins: [
          { x: 20, y: 18, label: "Bloque Verde: Proformas centralizadas del periodo ($7.600.000)" },
          { x: 55, y: 18, label: "Bloque Gris: Proformas pendientes o fuera de periodo ($0)" }
        ],`;

const t2 = `        pins: [
          { x: 50, y: 45, label: "Asiento de cierre: Débitos agrupados por CC y crédito a pasivo con auxiliar RUT" }
        ],`;
const r2 = `        pins: [
          { x: 50, y: 32, label: "Asiento formal generado (#20260009): Débitos agrupados por CC y crédito con auxiliar RUT 76.111.222-3" }
        ],`;

file = file.replace(/\r\n/g, '\n');
if (file.includes(t1.replace(/\r\n/g, '\n'))) {
  file = file.replace(t1.replace(/\r\n/g, '\n'), r1.replace(/\r\n/g, '\n'));
  console.log('Step 3.4 pins updated');
}
if (file.includes(t2.replace(/\r\n/g, '\n'))) {
  file = file.replace(t2.replace(/\r\n/g, '\n'), r2.replace(/\r\n/g, '\n'));
  console.log('Step 3.5 pins updated');
}

fs.writeFileSync('docs/sesiones/compras-mejoras-modulo2-2026-10-30/recorrido.html', file.replace(/\n/g, '\r\n'), 'utf8');
console.log('recorrido.html Phase 2 updated.');

