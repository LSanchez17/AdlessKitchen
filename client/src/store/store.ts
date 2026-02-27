import { configureStore } from '@reduxjs/toolkit'
import configureMiddleWare from './middleware'
import applicationReducer from './root_reducer'

const store = configureStore({
    reducer: applicationReducer,
    middleware: (gdm) => configureMiddleWare(gdm),
    devTools: import.meta.env.VITE_ENVIRONMENT !== "production",
})

// Infer the `RootState` and `AppDispatch` types from the store itself
type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
type AppDispatch = typeof store.dispatch

export type { RootState, AppDispatch }
export default store;