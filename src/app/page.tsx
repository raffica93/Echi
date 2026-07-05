import Image from "next/image";
import { ArrowRight, LockKeyhole, Mail, TimerReset } from "lucide-react";
import { Button } from "@/components/ui/button";

const steps = [
  {
    label: "Scrivi",
    text: "Lascia testo e media senza trasformarli in una lista di obiettivi.",
    icon: TimerReset,
  },
  {
    label: "Sigilla",
    text: "Dopo il sigillo, il contenuto non potra piu essere modificato.",
    icon: LockKeyhole,
  },
  {
    label: "Ricevi",
    text: "Una mail ti riportera qui quando sara il momento.",
    icon: Mail,
  },
];

export default function Home() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#111216] text-white">
      <section className="relative isolate flex min-h-screen items-center">
        <Image
          src="/images/eco-capsule-hero.png"
          alt=""
          fill
          priority
          sizes="100vw"
          className="absolute inset-0 -z-20 object-cover"
        />
        <div className="hero-vignette absolute inset-0 -z-10" />

        <div className="container grid min-h-screen items-center py-8 sm:py-10">
          <div className="max-w-3xl pt-12 sm:pt-0">
            <p className="mb-5 w-fit border border-white/24 bg-black/24 px-3 py-1 text-xs uppercase tracking-[0.28em] text-[#d8c49e]">
              Prodotto 0
            </p>
            <h1 className="font-display text-[clamp(4rem,12vw,11rem)] font-semibold leading-[0.78] tracking-normal text-white">
              Eco
            </h1>
            <p className="mt-8 max-w-2xl text-balance text-2xl leading-snug text-[#f3efe5] sm:text-4xl">
              Una macchina del tempo per le cose che vuoi lasciare al futuro.
            </p>
            <div className="mt-10 flex flex-col gap-3 sm:flex-row">
              <Button asChild size="lg">
                <a href="/crea" aria-label="Crea il tuo Eco">
                  Crea il tuo Eco
                  <ArrowRight aria-hidden="true" className="size-4" />
                </a>
              </Button>
              <Button asChild size="lg" variant="secondary">
                <a href="#rituale">Vedi il rituale</a>
              </Button>
            </div>
          </div>

          <div
            id="rituale"
            className="mt-auto grid gap-3 border-t border-white/18 pt-5 sm:grid-cols-3"
            aria-label="Passaggi del rituale"
          >
            {steps.map((step) => (
              <div
                key={step.label}
                className="flex min-h-24 gap-3 border border-white/16 bg-black/28 p-4 backdrop-blur-md"
              >
                <step.icon
                  aria-hidden="true"
                  className="mt-1 size-5 shrink-0 text-[#d8c49e]"
                />
                <div>
                  <h2 className="font-sans text-sm font-semibold text-white">
                    {step.label}
                  </h2>
                  <p className="mt-1 text-sm leading-6 text-white/72">
                    {step.text}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
