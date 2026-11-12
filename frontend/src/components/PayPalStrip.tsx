import { PAYPAL_ONLY } from '../lib/flags'

/** Judging build only: says plainly that PayPal is the only payment rail and how each part is used. */
export function PayPalStrip() {
  if (!PAYPAL_ONLY) return null
  const parts = [
    ['Payouts API', 'pays approved purchases'],
    ['Orders', 'a person approves bigger ones in PayPal'],
    ['Webhooks', 'confirm every payment before Flaire records it'],
  ]
  return (
    <section className="rounded-[18px] border border-[#D9CCF5] bg-[#F4EEFD] px-6 py-4 flex flex-wrap items-center gap-x-8 gap-y-3">
      <div>
        <div className="text-[15px] font-bold text-[#2E0F6B]">Every payment in Flaire runs through PayPal</div>
        <div className="text-[13px] text-[#5B4A86]">Built for the PayPal AI Hackathon. Sandbox only, no real money moves.</div>
      </div>
      <ul className="flex flex-wrap gap-x-6 gap-y-1.5 text-[13.5px] text-[#2E0F6B]">
        {parts.map(([a, b]) => (
          <li key={a}><span className="font-semibold">{a}</span> <span className="text-[#5B4A86]">{b}</span></li>
        ))}
      </ul>
    </section>
  )
}
