defmodule Project1.MixProject do
  use Mix.Project

  def project do
    [
      app: :project_1,
      version: "0.1.0",
      elixir: "~> 1.14",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger]
    ]
  end

  defp deps do
    [
      {:jason, "~> 1.4.0"},
    ]
  end
end
