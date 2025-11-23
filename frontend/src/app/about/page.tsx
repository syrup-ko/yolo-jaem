"use client";

export default function AboutPage() {
  return (
    <section className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-3">소개</h2>
      <p className="text-gray-700 mb-4">
        YOLO-JAEM은 Stock, HYSA, 부동산의 수익률을 비교하는 시뮬레이터입니다.
      </p>
      <ul className="list-disc list-inside space-y-2 text-gray-600">
        <li>SSR/SSG 가능한 Next.js(App Router)</li>
        <li>FastAPI 기반 Simulation API</li>
        <li>Redis 캐시, TimescaleDB 시계열 저장</li>
      </ul>
    </section>
  );
}



