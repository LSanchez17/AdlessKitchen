import type { PayloadAction } from '@reduxjs/toolkit';
import { createSlice } from '@reduxjs/toolkit';
import type { AuthState } from '../global/types';
import type { User } from './types';


const initialState: AuthState = {
    user: null
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        logout(state) {
            state.user = null;
        },
        setUser(state, action: PayloadAction<User | null>) {
            state.user = action.payload;
        },
    },
});

export const { logout, setUser } = userSlice.actions;

export const selectCurrentUser = (state: { user: AuthState }) => state.user.user;
export const selectIsUserLoggedIn = (state: { user: AuthState }) => !!state.user.user?.token;

export default userSlice.reducer;
