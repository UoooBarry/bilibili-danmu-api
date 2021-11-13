import service from "./service";

export const getDanmus = (bv) => {
  return service.get(`/danmus/${bv}`);
}
