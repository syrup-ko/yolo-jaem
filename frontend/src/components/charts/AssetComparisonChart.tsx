"use client";
import { SimulationResult } from "../../features/simulation/types";
import LineChart from "./LineChart";

type Props = { data: SimulationResult };

export default function AssetComparisonChart({ data }: Props) {
  const labels = data.timeline.map((p) => p.date);
  const series = data.assets.map((a) => ({
    name: a.name,
    data: a.values
  }));
  return <LineChart labels={labels} series={series} />;
}



