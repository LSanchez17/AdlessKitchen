import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useExtractRecipeFromUrlMutation } from "@/api/endpoints/recipes/recipes_api";

const Home = () => {
    const [url, setUrl] = useState("");
    const [urlError, setUrlError] = useState("");
    const [taskId, setTaskId] = useState<string | null>(null);

    const [extractRecipe, { isLoading }] = useExtractRecipeFromUrlMutation();

    const handleSubmit = async () => {
        setUrlError("");

        if (!url.startsWith("https://")) {
            setUrlError("URL must start with 'https://'");
            return;
        }

        try {
            const response = await extractRecipe({ url }).unwrap();
            setTaskId(response.results[0]?.taskId ?? null);
            setUrl("");
        } catch {
            setUrlError("Failed to submit URL. Please try again.");
        }
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") {
            handleSubmit();
        }
    };

    return (
        <div className="min-h-screen bg-gray-900 p-8">
            <div className="max-w-6xl mx-auto">
                <h1 className="text-3xl font-bold text-gray-100 mb-8">Dashboard</h1>

                {/* Recipe URL import */}
                <div className="bg-gray-800 rounded-lg shadow p-6 mb-8">
                    <h2 className="text-lg font-semibold text-gray-100 mb-4">
                        Import a Recipe
                    </h2>
                    <p className="text-sm text-gray-400 mb-4">
                        Paste a recipe URL and we'll gather the ingredients and instructions for you.
                    </p>

                    <div className="flex gap-3">
                        <input
                            type="url"
                            value={url}
                            onChange={(e) => {
                                setUrl(e.target.value);
                                setUrlError("");
                                setTaskId(null);
                            }}
                            onKeyDown={handleKeyDown}
                            placeholder="https://..."
                            className="flex-1 rounded-md bg-gray-700 border border-gray-600 text-gray-100 placeholder-gray-500 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent"
                        />
                        <Button
                            variant="secondary"
                            onClick={handleSubmit}
                            disabled={isLoading}
                        >
                            {isLoading ? "Submitting..." : "Import"}
                        </Button>
                    </div>

                    {urlError && (
                        <p className="mt-2 text-sm text-red-400">{urlError}</p>
                    )}

                    {taskId && (
                        <p className="mt-2 text-sm text-green-400">
                            Recipe extraction started — task ID: <span className="font-mono">{taskId}</span>
                        </p>
                    )}
                </div>

                {/* Placeholder cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div className="bg-gray-800 rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-700 rounded flex items-center justify-center text-gray-500">
                            Card 1
                        </div>
                    </div>

                    <div className="bg-gray-800 rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-700 rounded flex items-center justify-center text-gray-500">
                            Card 2
                        </div>
                    </div>

                    <div className="bg-gray-800 rounded-lg shadow p-6">
                        <div className="h-40 bg-gray-700 rounded flex items-center justify-center text-gray-500">
                            Card 3
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;