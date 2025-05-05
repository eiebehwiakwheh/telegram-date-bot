import { useState } from "react";

function calculateEaster(year) {
  const a = year % 19;
  const b = Math.floor(year / 100);
  const c = year % 100;
  const d = Math.floor(b / 4);
  const e = b % 4;
  const f = Math.floor((b + 8) / 25);
  const g = Math.floor((b - f + 1) / 3);
  const h = (19 * a + b - d - g + 15) % 30;
  const i = Math.floor(c / 4);
  const k = c % 4;
  const l = (32 + 2 * e + 2 * i - h - k) % 7;
  const m = Math.floor((a + 11 * h + 22 * l) / 451);
  const month = Math.floor((h + l - 7 * m + 114) / 31);
  const day = ((h + l - 7 * m + 114) % 31) + 1;
  return new Date(year, month - 1, day);
}

function formatDate(date) {
  return date.toLocaleDateString("en-GB", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export default function App() {
  const [year, setYear] = useState(2025);
  const [dates, setDates] = useState(null);

  const handleCalculate = () => {
    const easter = calculateEaster(year);
    const ash = new Date(easter);
    ash.setDate(easter.getDate() - 46);
    const pentecost = new Date(easter);
    pentecost.setDate(easter.getDate() + 49);

    setDates({
      ash: formatDate(ash),
      easter: formatDate(easter),
      pentecost: formatDate(pentecost),
    });
  };

  return (
    <div className="p-4 max-w-md mx-auto space-y-4 text-center">
      <h1 className="text-2xl font-semibold">Liturgical Dates Finder</h1>
      <div className="flex gap-2 justify-center">
        <input
          type="number"
          value={year}
          min={1583}
          max={9999}
          onChange={(e) => setYear(parseInt(e.target.value))}
          className="border rounded px-3 py-2 w-32"
        />
        <button
          onClick={handleCalculate}
          className="bg-blue-600 text-white rounded px-4 py-2"
        >
          Calculate
        </button>
      </div>

      {dates && (
        <div className="bg-white rounded shadow p-4 text-left">
          <p><strong>Ash Wednesday:</strong> {dates.ash}</p>
          <p><strong>Easter Sunday:</strong> {dates.easter}</p>
          <p><strong>Pentecost:</strong> {dates.pentecost}</p>
        </div>
      )}
    </div>
  );
}