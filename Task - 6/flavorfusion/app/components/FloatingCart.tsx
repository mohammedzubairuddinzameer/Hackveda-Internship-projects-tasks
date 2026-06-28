"use client";
import { useCart } from "../context/CartContext";
import { useRouter } from "next/navigation";

export default function FloatingCart() {
  const { cart } = useCart();
  const router = useRouter();

  const count = cart.reduce((acc, item) => acc + item.quantity, 0);

  return (
    <button
      onClick={() => router.push("/cart")}
      className="fixed bottom-6 left-6 bg-orange-500 text-white px-5 py-3 rounded-full shadow-xl z-50 hover:scale-105 transition"
    >
      🛒 {count}
    </button>
  );
}