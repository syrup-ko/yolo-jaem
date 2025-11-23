"use client";

type Props = {
  value: number;
  onChange: (value: number) => void;
};

export default function YoloJaemInput({ value, onChange }: Props) {
  return (
    <div>
      <label className="block text-sm font-semibold text-gray-700 mb-2">
        월 납입액 (원)
      </label>
      <input
        type="number"
        min={0}
        value={value}
        onChange={(e) => onChange(parseInt(e.target.value || "0", 10))}
        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        placeholder="500,000"
      />
    </div>
  );
}
