"use client";
import { ASSET_OPTIONS } from "../../lib/constants";

type Props = {
  value: string[];
  onChange: (value: string[]) => void;
};

export default function AssetInput({ value, onChange }: Props) {
  const toggle = (asset: string) => {
    const set = new Set(value);
    if (set.has(asset)) set.delete(asset);
    else set.add(asset);
    onChange(Array.from(set));
  };

  return (
    <div>
      <label className="block text-sm font-semibold text-gray-700 mb-2">
        자산 선택 (2개 이상)
      </label>
      <div className="flex gap-3 flex-wrap">
        {ASSET_OPTIONS.map((a) => (
          <button
            key={a}
            type="button"
            onClick={() => toggle(a)}
            className={`px-4 py-2 rounded-lg font-medium transition-all ${
              value.includes(a)
                ? "bg-blue-100 border-2 border-blue-600 text-blue-700"
                : "bg-white border border-gray-300 text-gray-700 hover:border-gray-400"
            }`}
          >
            {a}
          </button>
        ))}
      </div>
    </div>
  );
}
