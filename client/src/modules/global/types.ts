import type { User } from "../user/types";

interface AuthState {
    user: User | null;
};

export type { AuthState }