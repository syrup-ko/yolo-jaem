"use client";
import AssetInput from "../components/inputs/AssetInput";
import DurationInput from "../components/inputs/DurationInput";
import CapitalInput from "../components/inputs/CapitalInput";
import YoloJaemInput from "../components/inputs/YoloJaemInput";
import { useSimulationStore } from "../store/simulationStore";
import { runSimulation } from "../services/simulationService";

export default function HomePage() {
  const { input, setInput, setResult } = useSimulationStore();

  const handleSimulate = async () => {
    const result = await runSimulation(input);
    setResult(result);
    window.location.href = "/results";
  };

  return (
    <section className="bg-white rounded-lg shadow-sm p-6">
      <h1 className="text-3xl font-bold text-gray-900 mb-2">YOLO-JAEM 시뮬레이터</h1>
      <p className="text-gray-600 mb-6">두 개 이상의 자산을 비교하고 수익률 차트를 확인하세요.</p>
      <div className="grid gap-6">
        <AssetInput value={input.assets} onChange={(v) => setInput({ assets: v })} />
        <DurationInput value={input.durationYears} onChange={(v) => setInput({ durationYears: v })} />
        <CapitalInput value={input.initialCapital} onChange={(v) => setInput({ initialCapital: v })} />
        <YoloJaemInput value={input.monthlyContribution} onChange={(v) => setInput({ monthlyContribution: v })} />
        <button 
          onClick={handleSimulate} 
          className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-lg transition-colors"
        >
          시뮬레이션 실행
        </button>
      </div>
    </section>
  );
}



