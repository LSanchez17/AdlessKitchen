interface Recipe {
    id?: string;
    user_id?: string;
    title?: string;
    ingredients?: string[];
    steps?: string[];
    created_at?: string;
    updated_at?: string;
}

export type { Recipe };
