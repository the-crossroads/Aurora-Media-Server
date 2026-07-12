import { useQuery } from '@tanstack/react-query';

async function fetchOverview() {
  const response = await fetch('/api/dashboard/overview');
  if (!response.ok) throw new Error('Failed to load dashboard');
  return response.json();
}

export default function DashboardPage() {
  const { data, isLoading, error } = useQuery({ queryKey: ['overview'], queryFn: fetchOverview });

  if (isLoading) return <div className="text-slate-300">Loading dashboard…</div>;
  if (error) return <div className="text-rose-400">Unable to load dashboard</div>;

  return (
    <div className="grid gap-6 lg:grid-cols-3">
      <section className="rounded-2xl border border-white/10 bg-slate-900/80 p-6">
        <h3 className="mb-4 text-lg font-semibold">Continue watching</h3>
        <ul className="space-y-2 text-slate-300">
          {(data.continue_watching as string[]).map((item) => (
            <li key={item} className="rounded-lg border border-white/10 bg-slate-800/70 px-3 py-2">{item}</li>
          ))}
        </ul>
      </section>
      <section className="rounded-2xl border border-white/10 bg-slate-900/80 p-6">
        <h3 className="mb-4 text-lg font-semibold">Recently added</h3>
        <ul className="space-y-2 text-slate-300">
          {(data.recently_added as string[]).map((item) => (
            <li key={item} className="rounded-lg border border-white/10 bg-slate-800/70 px-3 py-2">{item}</li>
          ))}
        </ul>
      </section>
      <section className="rounded-2xl border border-white/10 bg-slate-900/80 p-6">
        <h3 className="mb-4 text-lg font-semibold">Statistics</h3>
        <p className="text-4xl font-semibold text-cyan-400">{data.stats}</p>
      </section>
    </div>
  );
}
