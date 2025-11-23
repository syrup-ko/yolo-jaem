import { useSimulationStore } from "../../../store/simulationStore";
import { runSimulation } from "../../../services/simulationService";

export function useSimulation() {
  const { input, setResult } = useSimulationStore();
  const simulate = async () => {
    const res = await runSimulation(input);
    setResult(res);
  };
  return { simulate };
}



