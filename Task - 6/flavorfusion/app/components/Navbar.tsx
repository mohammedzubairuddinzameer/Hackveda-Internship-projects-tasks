"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useCart } from "../context/CartContext";

export default function Navbar() {
  const pathname = usePathname();
  const { cart } = useCart();

  const count = cart.reduce((acc, item) => acc + item.quantity, 0);

  const linkClass = (path: string) =>
    `relative px-4 py-2 rounded-lg transition ${
      pathname === path
        ? "bg-white text-orange-600 font-semibold"
        : "text-white hover:bg-white/20"
    }`;

  return (
    <div className="fixed top-0 left-0 w-full z-50 bg-gradient-to-r from-red-500 via-orange-500 to-amber-400 shadow-md">
      <div className="max-w-7xl mx-auto flex justify-between items-center px-6 py-3">

        {/* LOGO */}
        <div className="bg-white/20 px-4 py-2 rounded-lg font-bold text-white">
          FlavorFusion
        </div>

        {/* LINKS */}
        <div className="flex gap-4 items-center">
          <Link href="/" className={linkClass("/")}>
            Home
          </Link>

          <Link href="/menu" className={linkClass("/menu")}>
            Menu
          </Link>

          {/* CART WITH BADGE */}
          <Link href="/cart" className={linkClass("/cart")}>
            Cart
            {count > 0 && (
              <span className="absolute -top-2 -right-2 bg-white text-red-500 text-xs px-2 py-0.5 rounded-full font-bold">
                {count}
              </span>
            )}
          </Link>
        </div>
      </div>
    </div>
  );
}