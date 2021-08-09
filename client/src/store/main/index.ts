import { mutations } from './mutations'
import { getters } from './getters'
import { actions } from './actions'
import { MainState } from './state'

const defaultState: MainState = {
  document: undefined,
  files: [],
  flags: []
}

export const mainModule = {
  state: defaultState,
  mutations,
  actions,
  getters
}
