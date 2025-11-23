"use client";
import Link from "next/link";

export default function Navbar() {
  return (
    <header className="border-b border-gray-200 py-3">
      <nav className="max-w-4xl mx-auto flex gap-6 px-4">
        <Link
          href="/"
          className="font-semibold text-lg text-blue-600 hover:text-blue-700"
        >
          YOLO-JAEM
        </Link>
        <Link href="/results" className="text-gray-700 hover:text-gray-900">
          결과
        </Link>
        <Link href="/about" className="text-gray-700 hover:text-gray-900">
          소개
        </Link>
      </nav>
    </header>
  );
}
