import { useState } from "react"
import { Button } from "@/components/ui/button"

function App() {
  const [link, setLink] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // rtk hook goes hereeee
    console.log("submitted link", link)
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-4 bg-gradient-to-br from-blue-500 to-purple-600">
      <h1 className="text-4xl font-bold mb-4">Welcome to Adless Kitchen</h1>
      <p className="text-center max-w-xl text-gray-700 mb-8">
        Paste a recipe URL and let our chef strip away the ads and junk so you can
        focus on cooking delicious meals without distractions.
      </p>

      <form onSubmit={handleSubmit} className="w-full max-w-lg">
        <div className="flex gap-2">
          <input
            type="url"
            value={link}
            onChange={(e) => setLink(e.target.value)}
            placeholder="Enter recipe link"
            className="flex-1 px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <Button type="submit">Go</Button>
        </div>
      </form>
    </main>
  )
}

export default App
