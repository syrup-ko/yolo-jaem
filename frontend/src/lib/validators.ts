export function ensureAtLeastTwoAssets(assets: string[]) {
  if (!assets || assets.length < 2) {
    throw new Error("자산은 최소 2개 이상 선택해야 합니다.");
  }
}



