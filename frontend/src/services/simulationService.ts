import { SimulationInput, SimulationResult } from "../features/simulation/types";
import { apiPost } from "./apiClient";

export async function runSimulation(input: SimulationInput): Promise<SimulationResult> {
  return apiPost<SimulationResult>("/api/v1/simulate", input);
}



