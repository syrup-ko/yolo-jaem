import { SimulationResult } from "./types";

export function formatResultForChart(res: SimulationResult) {
  return {
    labels: res.timeline.map((p) => p.date),
    series: res.assets.map((a) => ({ name: a.name, data: a.values }))
  };
}



