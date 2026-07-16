"use client";

import { useEffect, useState } from "react";

type Product = {
  id: number;
  name: string;
};

export default function Home() {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/products`)
      .then((response) => response.json())
      .then((data) => setProducts(data));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        ShopSphere Products
      </h1>

      <div className="space-y-4">
        {products.map((product) => (
          <div
            key={product.id}
            className="border p-4 rounded"
          >
            {product.name}
          </div>
        ))}
      </div>
    </main>
  );
}
