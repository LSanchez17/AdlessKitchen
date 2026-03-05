import type { Recipe } from '@/modules/recipes/types';
import type { Response } from '@/api/types';
import api from '@/api/api';

const recipeApi = api.injectEndpoints({
    endpoints: (build) => ({
        getRecipes: build.query<Response<Recipe>, void>({
            query: () => 'recipes',
        }),
        addRecipe: build.mutation<Response<Recipe>, Partial<Recipe>>({
            query: (body) => ({ url: 'recipes', method: 'POST', body }),
        }),
    }),
    overrideExisting: false,
});

export const { useGetRecipesQuery, useAddRecipeMutation } = recipeApi;
export { recipeApi };
