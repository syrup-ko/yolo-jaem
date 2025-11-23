"use client";
import { useEffect } from "react";
import { useSimulationStore } from "../../store/simulationStore";
import AssetComparisonChart from "../../components/charts/AssetComparisonChart";

export default function ResultsPage() {
  const { result } = useSimulationStore();

  useEffect(() => {
    if (!result) {
      window.location.href = "/";
    }
  }, [result]);

  if (!result) return null;

  return (
    <section className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-2">시뮬레이션 결과</h2>
      <p className="text-gray-600 mb-6">
        자산별 누적 가치 및 주요 지표를 확인하세요.
      </p>
      <AssetComparisonChart data={result} />
    </section>
  );
}
