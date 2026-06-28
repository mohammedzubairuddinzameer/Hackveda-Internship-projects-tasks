"use client";

import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import { useCart } from "../context/CartContext";
import { mockDishes } from "./mockDishes";
import FloatingCart from "../components/FloatingCart";

export default function MenuPage() {
  const { addToCart } = useCart();

  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [toast, setToast] = useState("");

  useEffect(() => {
    if (toast) {
      const timer = setTimeout(() => setToast(""), 2000);
      return () => clearTimeout(timer);
    }
  }, [toast]);

  const categories = [
    "All",
    "Roti",
    "Rice",
    "Curry",
    "Sweets",
    "Fast Food",
    "Others",
  ];

  const filtered =
    category === "All"
      ? mockDishes
      : mockDishes.filter((d) => d.category === category);

  const finalDishes = filtered.filter((d) =>
    d.title.toLowerCase().includes(search.toLowerCase())
  );

  const handleAdd = (dish: any) => {
    addToCart({ ...dish, quantity: 1 });
    setToast(`${dish.title} added to cart!`);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-orange-100 via-red-100 to-yellow-100">

      {/* ✅ NAVBAR */}
      <Navbar />

      <section className="px-6 pt-24 pb-10 max-w-7xl mx-auto animate-fadeIn">

        {/* 🔥 TITLE */}
        <h1 className="text-3xl font-bold text-red-600 mb-8">
          Explore Our Menu 🍽️
        </h1>

        {/* 🔍 SEARCH BAR */}
        <input
          type="text"
          placeholder="Search delicious food..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full p-3 rounded-xl border shadow-sm mb-6 focus:outline-none focus:ring-2 focus:ring-orange-400 transition"
        />

        {/* 🎯 CATEGORY BUTTONS */}
        <div className="sticky top-16 z-40 bg-white shadow-sm py-3 mb-4 overflow-x-auto">
  <div className="flex gap-3 px-4 min-w-max">
    {categories.map((c) => (
      <button
        key={c}
        onClick={() => setCategory(c)}
        className={`px-4 py-2 rounded-full text-sm font-medium transition ${
          category === c
            ? "bg-gradient-to-r from-red-500 to-orange-500 text-white"
            : "bg-gray-100 hover:bg-orange-200"
        }`}
      >
        {c}
      </button>
    ))}
  </div>
</div>

        {/* 🍱 GRID */}
        <div className="grid grid-cols-2 md:grid-cols-3 gap-6">
          {finalDishes.map((dish) => (
            <div
              key={dish.id}
              className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-2xl hover:scale-[1.04] transition duration-300"
            >
              {/* IMAGE */}
              <div className="h-40 overflow-hidden">
                <img
                  src={dish.image}
                  alt={dish.title}
                  className="w-full h-full object-cover hover:scale-110 transition duration-300"
                />
              </div>

              {/* CONTENT */}
              <div className="p-4">
                <h3 className="font-semibold text-gray-800">
                  {dish.title}
                  <p className="text-yellow-500 text-sm">⭐ 4.3</p>
                </h3>

                <div className="flex justify-between items-center mt-3">
                  <span className="text-red-600 font-bold text-lg">
                    ₹ {dish.price}
                  </span>

                  <button
                    onClick={() => handleAdd(dish)}
                    className="bg-gradient-to-r from-red-500 to-orange-500 text-white px-3 py-1 rounded-lg text-sm shadow hover:scale-105 active:scale-95 transition"
                  >
                    Add
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>

      </section>

      {/* ✅ TOAST (UPGRADED UI) */}
      {toast !== "" && (
        <div
          style={{
            position: "fixed",
            top: "20px",
            right: "20px",
            background: "green",
            color: "white",
            padding: "12px 20px",
            borderRadius: "8px",
            zIndex: 9999,
            fontWeight: "bold",
          }}
        >
          {toast}
        </div>
      )}

      <FloatingCart />

    </main>
  );
}