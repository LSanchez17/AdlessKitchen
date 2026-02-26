/**
 * Represents the structure of a response from the API.
 * The `entity` field indicates the type of data returned (e.g., "user", "recipes").
 * The `results` field contains the actual data, which is always an array of objects, even if the array contains only a single item.
 */
interface Response<T> {
    entity: string;
    results: T[];
}

export type { Response }