const { ethers } = require("hardhat");

async function main() {
  const TEKUPToken = await ethers.getContractFactory("TEKUPToken");

  const initialSupply = ethers.utils.parseUnits("1000000", 18);

  const token = await TEKUPToken.deploy(initialSupply);
  await token.deployed();

  console.log("TEKUPToken deployed at:", token.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
