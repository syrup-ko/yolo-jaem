export type SimulationInput = {
  assets: string[];
  durationYears: number;
  initialCapital: number;
  monthlyContribution: number;
};

export type SimulationTimelinePoint = {
  date: string;
  total: number;
};

export type SimulationAssetSeries = {
  name: string;
  values: number[];
  cagr?: number;
  mdd?: number;
};

export type SimulationResult = {
  timeline: SimulationTimelinePoint[];
  assets: SimulationAssetSeries[];
};



