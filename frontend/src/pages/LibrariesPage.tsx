import { useQuery } from '@tanstack/react-query';

async function fetchLibraries() {
  const response = await fetch('/api/libraries');
  if (!response.ok) throw new Error('Failed to load libraries');
  return response.json();
}

export default function LibrariesPage() {
  const { data, isLoading, error } = useQuery({ queryKey: ['libraries'], queryFn: fetchLibraries });

  if (isLoading) return <div className="text-slate-300">Loading libraries…</div>;
  if (error) return <div className="text-rose-400">Unable to load libraries</div>;

  return (
    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
      {(data as Array<{ id: number; name: string; library_type: string; folder_path: string }>)?.map((library) => (
        <article key={library.id} className="rounded-2xl border border-white/10 bg-slate-900/80 p-6 shadow-lg shadow-slate-950/20">
          <h3 className="mb-2 text-xl font-semibold">{library.name}</h3>
          <p className="mb-2 text-sm uppercase tracking-[0.2em] text-cyan-400">{library.library_type}</p>
          <p className="text-sm text-slate-400">{library.folder_path}</p>
        </article>
      ))}
    </div>
  );
}
