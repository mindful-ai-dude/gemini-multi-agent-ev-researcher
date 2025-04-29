import React from 'react';

interface ReportResultsProps {
  report: any;
}

export function ReportResults({ report }: ReportResultsProps) {
  // This is a basic placeholder; you can expand this to show more details
  return (
    <div className="bg-white rounded shadow p-6 mt-6 w-full max-w-2xl">
      <h2 className="text-2xl font-semibold mb-4">Report Summary</h2>
      <div className="overflow-x-auto">
        <pre className="whitespace-pre-wrap break-words text-sm bg-gray-100 p-3 rounded max-w-full" style={{ wordBreak: 'break-word', whiteSpace: 'pre-wrap' }}>
          {JSON.stringify(report, null, 2)}
        </pre>
      </div>
      {report?.output_files && (
        <div className="mt-4">
          <h3 className="text-lg font-semibold mb-2">Downloadable Files</h3>
          <ul className="flex flex-wrap gap-3">
            {Object.entries(report.output_files).map(([key, path]) => (
              <li key={key}>
                <a
                  href={`/${path}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-xs font-medium transition"
                >
                  {key.replace('_', ' ').toUpperCase()}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
