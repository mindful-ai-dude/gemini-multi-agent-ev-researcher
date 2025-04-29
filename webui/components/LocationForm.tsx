import React, { useState } from 'react';

interface LocationFormProps {
  onSubmit: (city: string, state: string, country?: string) => void;
  loading: boolean;
}

export function LocationForm({ onSubmit, loading }: LocationFormProps) {
  const [city, setCity] = useState('');
  const [state, setState] = useState('');
  const [country, setCountry] = useState('');

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!city || !state) return;
    onSubmit(city, state, country || undefined);
  }

  return (
    <form className="bg-white rounded shadow p-6 flex flex-col gap-4 w-full max-w-md" onSubmit={handleSubmit}>
      <div>
        <label className="block mb-1 font-medium">City</label>
        <input
          className="w-full border rounded px-3 py-2"
          value={city}
          onChange={e => setCity(e.target.value)}
          placeholder="e.g. Austin"
          required
        />
      </div>
      <div>
        <label className="block mb-1 font-medium">State / Region</label>
        <input
          className="w-full border rounded px-3 py-2"
          value={state}
          onChange={e => setState(e.target.value)}
          placeholder="e.g. TX or Bavaria"
          required
        />
      </div>
      <div>
        <label className="block mb-1 font-medium">Country (optional, default USA)</label>
        <input
          className="w-full border rounded px-3 py-2"
          value={country}
          onChange={e => setCountry(e.target.value)}
          placeholder="e.g. USA or Morocco"
        />
      </div>
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Generating...' : 'Generate Report'}
      </button>
    </form>
  );
}
