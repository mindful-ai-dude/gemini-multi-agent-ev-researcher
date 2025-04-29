import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }
  const { city, state, country } = req.body;
  try {
    const backendRes = await fetch('http://localhost:8000/api/report', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ city, state, country }),
    });
    const data = await backendRes.json();
    res.status(backendRes.status).json(data);
  } catch (err: any) {
    res.status(500).json({ error: err.message || 'Backend connection failed' });
  }
}

