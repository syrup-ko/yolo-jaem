"use client";
type Props = {
  labels: string[];
  series: { name: string; data: number[] }[];
};
export default function LineChart({ labels, series }: Props) {
  // 실제 차트 라이브러리는 추후 적용 (e.g. Recharts, Chart.js)
  return (
    <div style={{ border: "1px dashed #ccc", padding: 16 }}>
      <strong>LineChart (placeholder)</strong>
      <div style={{ fontSize: 12, marginTop: 8 }}>
        labels: {labels.slice(0, 5).join(", ")}...
      </div>
      <div style={{ fontSize: 12 }}>
        series: {series.map((s) => s.name).join(", ")}
      </div>
    </div>
  );
}



