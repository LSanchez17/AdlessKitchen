
import { useState } from "react"
import { Button } from "@/components/ui/button"

const Signup = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = (e: React.SyntheticEvent<HTMLFormElement>) => {
        e.preventDefault()
        console.log("signup", email, password)
    }

    return (
        <div className="min-h-screen flex items-center justify-center px-4 bg-gray-900">
            <form onSubmit={handleSubmit} className="w-full max-w-md bg-gray-800 text-white p-8 rounded shadow">
                <h1 className="text-2xl font-bold mb-6 text-center">Create an account</h1>
                <div className="mb-4">
                    <label htmlFor="email" className="block text-gray-300 mb-1">
                        Email
                    </label>
                    <input
                        id="email"
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="w-full px-4 py-2 bg-gray-800 text-white border border-gray-700 rounded focus:outline-none focus:ring-2 focus:ring-red-500"
                    />
                </div>
                <div className="mb-6">
                    <label htmlFor="password" className="block text-gray-300 mb-1">
                        Password
                    </label>
                    <input
                        id="password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="w-full px-4 py-2 bg-gray-800 text-white border border-gray-700 rounded focus:outline-none focus:ring-2 focus:ring-red-500"
                    />
                </div>
                <Button type="submit" variant="secondary" className="w-full">
                    Sign up
                </Button>
            </form>
        </div>
    )
}

export default Signup