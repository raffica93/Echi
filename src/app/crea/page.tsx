import { ArrowLeft } from "lucide-react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function CreateEcoPage() {
  return (
    <main className="min-h-screen bg-[#e9e5da] text-[#111216]">
      <section className="container flex min-h-screen flex-col justify-center py-10">
        <Button asChild variant="ghost" className="mb-8 w-fit">
          <Link href="/">
            <ArrowLeft aria-hidden="true" className="size-4" />
            Indietro
          </Link>
        </Button>

        <div className="max-w-2xl">
          <p className="text-sm uppercase tracking-[0.24em] text-[#9b5f37]">
            Inizio
          </p>
          <h1 className="mt-4 font-display text-5xl font-semibold leading-none text-[#111216] sm:text-7xl">
            Cosa vuoi scaricare al mondo?
          </h1>
          <p className="mt-6 text-lg leading-8 text-[#3f4646]">
            Questo e il primo spazio del flow lineare. Qui entreranno identita
            leggera, bozza, media, anteprima, sigillo e scelta della data.
          </p>
        </div>
      </section>
    </main>
  );
}
