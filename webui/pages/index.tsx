import React, { useState } from 'react';
import { LocationForm } from '../components/LocationForm';
import { ReportResults } from '../components/ReportResults';

export default function HomePage() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(city: string, state: string, country?: string) {
    setLoading(true);
    setError(null);
    setReport(null);
    try {
      const res = await fetch('/api/report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city, state, country })
      });
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      setReport(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-4">
      <h1 className="text-3xl font-bold mb-6">EV Charging Infrastructure Research</h1>
      <LocationForm onSubmit={handleSubmit} loading={loading} />
      {error && <div className="mt-4 text-red-600">{error}</div>}
      {report && <ReportResults report={report} />}
    </main>
  );
}
