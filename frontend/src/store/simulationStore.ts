import { create } from "zustand";
import { SimulationInput, SimulationResult } from "../features/simulation/types";

type State = {
  input: SimulationInput;
  result?: SimulationResult;
  setInput: (partial: Partial<SimulationInput>) => void;
  setResult: (result?: SimulationResult) => void;
};

const defaultInput: SimulationInput = {
  assets: ["Stock", "HYSA"],
  durationYears: 10,
  initialCapital: 10000000,
  monthlyContribution: 500000
};

export const useSimulationStore = create<State>((set) => ({
  input: defaultInput,
  result: undefined,
  setInput: (partial) => set((s) => ({ input: { ...s.input, ...partial } })),
  setResult: (result) => set(() => ({ result }))
}));



