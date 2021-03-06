import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import SubmissionsHome from '@/submissions/views/SubmissionsHome.vue'
import Yield from '@/submissions/components/SubmissionForm/Yield.vue'

import { FETCH_CODES } from '@/submissions/store/actions.types.js'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(VueRouter)

const router = new VueRouter()

describe('SubmissionsHome.vue', () => {
  let actions
  let store

  beforeEach(() => {
    actions = {
      [FETCH_CODES]: jest.fn()
    }
    store = new Vuex.Store({
      state: {},
      actions
    })
  })

  it('triggers confirmation box when submitting the form', () => {
    const wrapper = shallowMount(SubmissionsHome, {
      localVue,
      store,
      router,
      sync: false
    })
    expect(wrapper.vm.confirmSubmitModal).toEqual(false)

    wrapper.find('form').trigger('submit')

    expect(wrapper.vm.confirmSubmitModal).toEqual(true)
  })

  it('requests codes/constants to use in form', () => {
    shallowMount(SubmissionsHome, {
      localVue,
      store,
      router,
      sync: false
    })
    expect(actions[FETCH_CODES]).toHaveBeenCalled()
  })

  it('renders components based on the activity selected (Yield exists on construction report, not on decommission report)', () => {
    const wrapper = shallowMount(SubmissionsHome, {
      localVue,
      store,
      router
    })
    wrapper.setData({ activityType: 'CON' })
    expect(wrapper.find(Yield).exists()).toBe(true)
    wrapper.setData({ activityType: 'DEC' })
    expect(wrapper.find(Yield).exists()).toBe(false)
  })
})
