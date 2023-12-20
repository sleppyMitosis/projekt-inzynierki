import { createRouter, createWebHistory } from "vue-router";
import { Route } from "@/router/route";
import LoginForm from "@/views/auth/login-form/LoginForm.vue";
import ResetPassword from "@/views/auth/new-user/NewUser.vue";
import DashboardView from "@/views/dashboard/DashboardView.vue"; // Import DashboardView
import main from "@/views/main/MainView.vue";
import SideMenu from "@/components/side-menu/SideMenu.vue";
import Calendar from "@/views/calendar/Calendar.vue";
import ProfileView from "@/views/profile/ProfileView.vue";
import FirstAidView from "@/views/first-aid/FirstAidView.vue";
import DragsView from "@/views/drugs/DragsView.vue";
import AnimalsView from "@/views/animals/AnimalsView.vue";
import NewUser from "@/views/auth/new-user/NewUser.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: Route.main.path,
      component: main,
      meta: { requiresAuth: true },
      children: [
        {
          path: Route.dashboard.path,
          components: {
            sideMenu: SideMenu,
            main: DashboardView,
          },
        },
        {
          path: Route.calendar.path,
          components: {
            sideMenu: SideMenu,
            main: Calendar,
          },
        },
        {
          path: Route.profile.path,
          components: {
            sideMenu: SideMenu,
            main: ProfileView,
          },
        },
        {
          path: Route.firstAid.path,
          components: {
            sideMenu: SideMenu,
            main: FirstAidView,
          },
        },
        {
          path: Route.drugs.path,
          components: {
            sideMenu: SideMenu,
            main: DragsView,
          },
        },
        {
          path: Route.animals.path,
          components: {
            sideMenu: SideMenu,
            main: AnimalsView,
          },
        },
      ],
    },
    {
      path: Route.newUser.path,
      component: NewUser,
      name: "newUser",
    },
    {
      path: Route.loginForm.path,
      component: LoginForm,
      name: "loginForm",
    },
  ],
});

export default router;
