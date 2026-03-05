import { useGetRecipesQuery } from '@/api/endpoints/recipe/recipe_api';
import RecipeCard from '@/components/recipeCard';

const RecipesPage = () => {
    const { data, isLoading, error } = useGetRecipesQuery();

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error loading recipes</div>;

    const recipes = data?.results ?? [];

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Your Recipes</h1>
            {recipes.length === 0 ? (
                <p>No recipes yet.</p>
            ) : (
                recipes.map((r) => <RecipeCard key={r.id} recipe={r} />)
            )}
        </div>
    );
};

export default RecipesPage;
