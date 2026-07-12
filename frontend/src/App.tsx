import { Link, Outlet } from 'react-router-dom';
import { motion } from 'framer-motion';

export default function App() {
  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.15),_transparent_30%),linear-gradient(135deg,_#020617_0%,_#0f172a_100%)] text-slate-100">
      <header className="border-b border-white/10 bg-slate-950/70 backdrop-blur">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Aurora</p>
            <h1 className="text-xl font-semibold">Media Server</h1>
          </div>
          <nav className="flex gap-4 text-sm text-slate-300">
            <Link to="/" className="transition hover:text-white">Dashboard</Link>
            <Link to="/libraries" className="transition hover:text-white">Libraries</Link>
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-6 py-10">
        <motion.section
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8 rounded-3xl border border-cyan-400/20 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/40"
        >
          <p className="mb-3 text-sm font-medium uppercase tracking-[0.3em] text-cyan-400">Self-hosted streaming</p>
          <h2 className="mb-4 text-3xl font-semibold">Organize, browse, and stream your personal library.</h2>
          <p className="max-w-2xl text-slate-300">
            Aurora combines the polish of modern media apps with a modular architecture designed for extension and long-term maintenance.
          </p>
        </motion.section>

        <Outlet />
      </main>
    </div>
  );
}
